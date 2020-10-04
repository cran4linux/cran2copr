%global packname  PML
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Penalized Multi-Band Learning for Circadian Rhythm AnalysisUsing Actigraphy

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rbokeh 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rbokeh 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 

%description
Penalized Multi-Band Learning algorithm can be effectively implemented for
circadian rhythm analysis and daily activity pattern characterization
using actigraphy (continuously measured objective physical activity data).
Functions for interactive visualization of actigraph data are also
included. Method reference: Li, X., Kane, M., Zhang, Y., Sun, W., Song,
Y., Dong, S., Lin, Q., Zhu, Q., Jiang, F., Zhao, H. (2019) A Novel
Penalized Multi-band Learning Approach Characterizes the Consolidation of
Sleep-Wake Circadian Rhythms During Early Childhood Development.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
