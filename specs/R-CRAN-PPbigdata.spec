%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PPbigdata
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Projection Pursuit for Big Data Based on Data Nuggets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-datanugget >= 1.2.4
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-rstiefel 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-tourr 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-datanugget >= 1.2.4
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-rstiefel 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-tourr 
Requires:         R-CRAN-mclust 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Perform 1-dim/2-dim projection pursuit, grand tour and guided tour for big
data based on data nuggets. Reference papers: [1] Beavers et al., (2024)
<doi:10.1080/10618600.2024.2341896>. [2] Duan, Y., Cabrera, J., & Emir, B.
(2023). "A New Projection Pursuit Index for Big Data."
<doi:10.48550/arXiv.2312.06465>.

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
