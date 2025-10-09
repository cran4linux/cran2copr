%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PVBcorrect
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Verification Bias Correction for Diagnostic Accuracy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-mice 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-mice 

%description
Performs partial verification bias (PVB) correction for binary diagnostic
tests, where PVB arises from selective patient verification in diagnostic
accuracy studies. Supports correction of important accuracy measures --
sensitivity, specificity, positive predictive values and negative
predictive value -- under missing-at-random and missing-not-at-random
missing data mechanisms. Available methods and references are "Begg and
Greenes' methods" in Alonzo & Pepe (2005)
<doi:10.1111/j.1467-9876.2005.00477.x> and deGroot et al. (2011)
<doi:10.1016/j.annepidem.2010.10.004>; "Multiple imputation" in Harel &
Zhou (2006) <doi:10.1002/sim.2494>, "EM-based logistic regression" in
Kosinski & Barnhart (2003) <doi:10.1111/1541-0420.00019>; "Inverse
probability weighting" in Alonzo & Pepe (2005)
<doi:10.1111/j.1467-9876.2005.00477.x>; "Inverse probability bootstrap
sampling" in Nahorniak et al. (2015) <doi:10.1371/journal.pone.0131765>
and Arifin & Yusof (2022) <doi:10.3390/diagnostics12112839>; "Scaled
inverse probability resampling methods" in Arifin & Yusof (2025)
<doi:10.1371/journal.pone.0321440>.

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
