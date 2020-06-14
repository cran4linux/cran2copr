%global packname  ExpertChoice
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Design of Discrete Choice and Conjoint Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-far 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DoE.base 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-far 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DoE.base 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-purrr 

%description
Supports designing efficient discrete choice experiments (DCEs).
Experimental designs can be formed on the basis of orthogonal arrays or
search methods for optimal designs (Federov or mixed integer programs).
Various methods for converting these experimental designs into a discrete
choice experiment. Many efficiency measures! Draws from literature of
Kuhfeld (2010) and Street et. al (2005)
<doi:10.1016/j.ijresmar.2005.09.003>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
