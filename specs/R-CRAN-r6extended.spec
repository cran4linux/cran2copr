%global packname  r6extended
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Extension for 'R6' Base Class

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.2.2
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-digest >= 0.6.12
BuildRequires:    R-CRAN-hellno >= 0.0.1
Requires:         R-CRAN-R6 >= 2.2.2
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-digest >= 0.6.12
Requires:         R-CRAN-hellno >= 0.0.1

%description
Useful methods and data fields to extend the bare bones 'R6' class
provided by the 'R6' package - ls-method, hashes, warning- and
message-method, general get-method and a debug-method that assigns self
and private to the global environment.

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
%{rlibdir}/%{packname}/INDEX
