%global __brp_check_rpaths %{nil}
%global packname  OptM
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating the Optimal Number of Migration Edges from 'Treemix'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-boot >= 1.3.20
BuildRequires:    R-CRAN-SiZer >= 0.1.4
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-boot >= 1.3.20
Requires:         R-CRAN-SiZer >= 0.1.4
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-grDevices 

%description
The popular population genetic software 'Treemix' by 'Pickrell and
Pritchard' (2012) <DOI:10.1371/journal.pgen.1002967> estimates the number
of migration edges on a population tree. However, it can be difficult to
determine the number of migration edges to include. Previously, it was
customary to stop adding migration edges when 99.8%% of variation in the
data was explained, but 'OptM' automates this process using an ad hoc
statistic based on the second-order rate of change in the log likelihood.
'OptM' also has added functionality for various threshold modeling to
compare with the ad hoc statistic.

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
