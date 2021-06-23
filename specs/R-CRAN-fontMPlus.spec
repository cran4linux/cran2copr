%global __brp_check_rpaths %{nil}
%global packname  fontMPlus
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Additional 'ggplot2' Themes Using 'M+' Fonts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 

%description
Provides 'ggplot2' themes based on the 'M+' fonts. The 'M+' fonts are a
font family under a free license. The font family provides multilingual
glyphs. The fonts provide 'Kana', over 5,000 'Kanji', Basic Latin, Latin-1
Supplement, Latin Extended-A, and 'IPA' Extensions glyphs. Most of the
Greek, Cyrillic, Vietnamese, and extended glyphs and symbols are included
too. So the fonts are in conformity with ISO-8859-1, 2, 3, 4, 5, 7, 9, 10,
13, 14, 15, 16, Windows-1252, T1, and VISCII encoding. More information
about the fonts can be found at
<http://mplus-fonts.osdn.jp/about-en.html>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/fonts
%{rlibdir}/%{packname}/INDEX
