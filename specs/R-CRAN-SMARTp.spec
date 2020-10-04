%global packname  SMARTp
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Sample Size for SMART Designs in Non-Surgical Periodontal Trials

License:          LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-sn >= 1.5
BuildRequires:    R-CRAN-mvtnorm >= 1.0
BuildRequires:    R-CRAN-covr 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-sn >= 1.5
Requires:         R-CRAN-mvtnorm >= 1.0
Requires:         R-CRAN-covr 
Requires:         R-stats 
Requires:         R-methods 

%description
Sample size calculation to detect dynamic treatment regime (DTR) effects
based on change in clinical attachment level (CAL) outcomes from a
non-surgical chronic periodontitis treatments study. The experiment is
performed under a Sequential Multiple Assignment Randomized Trial (SMART)
design. The clustered tooth (sub-unit) level CAL outcomes are skewed,
spatially-referenced, and non-randomly missing. The implemented algorithm
is available in Xu et al. (2019+) <arXiv:1902.09386>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
