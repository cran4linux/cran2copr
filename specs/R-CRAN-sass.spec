%global packname  sass
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Syntactically Awesome Style Sheets ('Sass')

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-htmltools 

%description
An 'SCSS' compiler, powered by the 'LibSass' library. With this, R
developers can use variables, inheritance, and functions to generate
dynamic style sheets. The package uses the 'Sass CSS' extension language,
which is stable, powerful, and CSS compatible.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/sass-color
%doc %{rlibdir}/%{packname}/sass-font
%doc %{rlibdir}/%{packname}/sass-size
%doc %{rlibdir}/%{packname}/sass-theme
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
