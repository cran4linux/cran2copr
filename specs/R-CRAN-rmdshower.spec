%global packname  rmdshower
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          'R' 'Markdown' Format for 'shower' Presentations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 0.3
Requires:         R-CRAN-rmarkdown >= 0.3

%description
'R' 'Markdown' format for 'shower' presentations, see
<https://github.com/shower/shower>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/auto-render.min.js
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/node_modules
%doc %{rlibdir}/%{packname}/package.json
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/style-common.css
%doc %{rlibdir}/%{packname}/style-earl2016.css
%doc %{rlibdir}/%{packname}/style-material.css
%doc %{rlibdir}/%{packname}/style-ribbon.css
%{rlibdir}/%{packname}/INDEX
