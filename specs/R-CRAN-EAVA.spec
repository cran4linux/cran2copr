%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EAVA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Deterministic Verbal Autopsy Coding with Expert Algorithm Verbal Autopsy

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 

%description
Expert Algorithm Verbal Autopsy assigns causes of death to 2016 WHO Verbal
Autopsy Questionnaire data. odk2EAVA() converts data to a standard input
format for cause of death determination building on the work of Thomas
(2021) <https://cran.r-project.org/src/contrib/Archive/CrossVA/>.
codEAVA() uses the presence and absence of signs and symptoms reported in
the Verbal Autopsy interview to diagnose common causes of death. A
deterministic algorithm assigns a single cause of death to each Verbal
Autopsy interview record using a hierarchy of all common causes for
neonates or children 1 to 59 months of age.

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
