%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OneArm2stage
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phase II Single-Arm Two-Stage Designs with Time-to-Event Outcomes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-IPDfromKM 
Requires:         R-CRAN-survival 
Requires:         R-utils 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-IPDfromKM 

%description
Two-stage design for single-arm phase II trials with time-to-event
endpoints (e.g., clinical trials on immunotherapies among cancer patients)
can be calculated using this package. Two notable advantages of the
package: 1) It provides flexible choices from three design methods
(optimal, minmax, and admissible), and 2) the power of the design is more
accurately calculated using the exact variance in the one-sample log-rank
test. The package can be used for 1) planning the sample sizes and other
design parameters, and 2) conducting the interim and final analyses for
the Go/No-go decisions. More details about the design method can be found
in: Wu, J, Chen L, Wei J, Weiss H, Chauhan A. (2020).
<doi:10.1002/pst.1983>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
