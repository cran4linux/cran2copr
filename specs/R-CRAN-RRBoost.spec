%global packname  RRBoost
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Robust Boosting Algorithm

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-RobStatTM 
Requires:         R-stats 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-RobStatTM 

%description
An implementation of robust boosting algorithms for regression in R. This
includes the RRBoost method proposed in the paper "Robust Boosting for
Regression Problems" (Ju X and Salibian-Barrera M. 2020)
<doi:10.1016/j.csda.2020.107065> (to appear in Computational Statistics
and Data Science). It also implements previously proposed boosting
algorithms in the simulation section of the paper: L2Boost, LADBoost,
MBoost (Friedman, J. H. (2001) <doi:10.1214/aos/1013203451>) and Robloss
(Lutz et al. (2008) <doi:10.1016/j.csda.2007.11.006>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
