import unicodedata

import streamlit as st

FORM = 'NFKC'

SAMPLE = '例：１２３ ①②③ ＡＢＣ ﾃｷｽﾄ ㍻ ㌔ ㈱ '

def main():
    st.set_page_config(
        page_title='Normalize',
        page_icon='☕',
        layout='wide'
    )
    st.title('Normalize')
    st.write('テキストのunicode正規化アプリ')

    col_from, col_to = st.columns(2, border=True)
    with col_from:
        st.write(':material/Check: テキストを入力してください')
        st.caption(f"{SAMPLE}")
        initial_height = 100
        text = st.text_area(
            label='_',
            height=initial_height,
            label_visibility='collapsed'
        )

    with col_to:
        st.write(':sparkles: unicode正規化したテキスト')
        st.caption(f"{unicodedata.normalize(FORM, SAMPLE)}")
        content = ''
        if not text:
            st.code(content, language=None)
        elif unicodedata.is_normalized(FORM, text):
            st.write('正規化されたテキストです')
        else:
            content = unicodedata.normalize(FORM, text)
            st.code(content, language=None)

    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("""
        * ブラウザ更新でリセットできます
        * NFKC 形式で正規化しています
        * unicode正規化の詳細については [Unicode正規化](https://ja.wikipedia.org/wiki/Unicode%E6%AD%A3%E8%A6%8F%E5%8C%96) 等でご確認ください
        """)
    with col_right:
        st.download_button(
            label='Download',
            data=content,
            file_name='normalized.txt',
            on_click='ignore',
            disabled=not content
        )


if __name__ == '__main__':
    main()
