%global packname  ezknitr
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          Avoid the Typical Working Directory Pain When Using 'knitr'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.7
BuildRequires:    R-CRAN-R.utils >= 1.34.0
BuildRequires:    R-CRAN-markdown >= 0.7
Requires:         R-CRAN-knitr >= 1.7
Requires:         R-CRAN-R.utils >= 1.34.0
Requires:         R-CRAN-markdown >= 0.7

%description
An extension of 'knitr' that adds flexibility in several ways. One common
source of frustration with 'knitr' is that it assumes the directory where
the source file lives should be the working directory, which is often not
true. 'ezknitr' addresses this problem by giving you complete control over
where all the inputs and outputs are, and adds several other convenient
features to make rendering markdown/HTML documents easier.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/joss
%{rlibdir}/%{packname}/INDEX
