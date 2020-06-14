%global packname  spherepc
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          2%{?dist}
Summary:          Spherical Principal Curves

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-sphereplot 
BuildRequires:    R-stats 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-sphereplot 
Requires:         R-stats 

%description
Fitting a principal curve to data lying in the spherical surface. This
package provides principal circle, principal geodesic analysis, Hauberg's
principal curves, and spherical principal curves. Moreover, it offers
locally defined principal geodesics which are currently under study. The
detailed procedures are described in Jang-Hyun Kim, Jongmin Lee and
Hee-Seok Oh (2020) <arXiv:2003.02578>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
