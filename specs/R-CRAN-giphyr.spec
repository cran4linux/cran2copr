%global packname  giphyr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          R Interface to the Giphy API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rstudioapi 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 

%description
An interface to the 'API' of 'Giphy', a popular index-based search engine
for 'GIFs' and animated stickers (see <http://giphy.com/faq> and
<https://github.com/Giphy/GiphyAPI> for more information about 'Giphy' and
its 'API') . This package also provides a 'RStudio Addin', which can help
users easily search and download 'GIFs' and insert them to a 'rmarkdown'
presentation.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/gadgets
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
