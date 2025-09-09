import unicodedata

import streamlit as st

FORM = 'NFKC'

SAMPLE = '１２３ ①②③ ＡＢＣ ﾃｷｽﾄ ㍻ ㌔ ㈱ '

def main():
    st.set_page_config(
        page_title='Normalize',
        page_icon='☕',
        layout='wide'
    )
    st.title('Normalize')
    st.markdown('テキストのunicode正規化アプリ')
    st.caption(f"例：「{SAMPLE}」 -> 「{unicodedata.normalize(FORM, SAMPLE)}」")

    col_from, col_to = st.columns(spec=2, border=True)
    with col_from:
        st.markdown(':memo: テキストを入力してください')
        initial_height = 100
        text = st.text_area(
            label='_',
            height=initial_height,
            label_visibility='collapsed'
        )

    with col_to:
        st.markdown(':sparkles: unicode正規化したテキスト')
        content = ''
        if not text:
            st.code(content, language=None)
        elif unicodedata.is_normalized(FORM, text):
            st.info('すでに正規化されたテキストです')
        else:
            content = unicodedata.normalize(FORM, text)
            st.code(content, language=None)

        st.download_button(
            label='Download',
            data=content,
            file_name='normalized.txt',
            on_click='ignore',
            disabled=not content
        )

    st.markdown("""
    * ブラウザ更新でリセットできます
    * NFKC 形式で正規化しています
    * unicode正規化の詳細については 
        [Unicode正規化](https://ja.wikipedia.org/wiki/Unicode%E6%AD%A3%E8%A6%8F%E5%8C%96)
        等でご確認ください
    """)


if __name__ == '__main__':
    main()
