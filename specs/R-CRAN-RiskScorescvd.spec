%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RiskScorescvd
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cardiovascular Risk Scores Calculator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-PooledCohort >= 0.0.1
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-PooledCohort >= 0.0.1

%description
A tool to calculate Cardiovascular Risk Scores in large data frames.
Cardiovascular risk scores are statistical tools used to assess an
individual's likelihood of developing a cardiovascular disease based on
various risk factors, such as age, gender, blood pressure, cholesterol
levels, and smoking. Here we bring together the six most commonly used in
the emergency department. Using 'RiskScorescvd', you can calculate all the
risk scores in an extended dataset in seconds. ASCVD described in Goff, et
al (2013) <doi:10.1161/01.cir.0000437741.48606.98>. EDACS described in
Mark DG, et al (2016) <doi:10.1016/j.jacc.2017.11.064>. GRACE described in
Fox KA, et al (2006) <doi:10.1136/bmj.38985.646481.55>. HEART is described
in Mahler SA, et al (2017) <doi:10.1016/j.clinbiochem.2017.01.003>.
SCORE2/OP described in SCORE2 working group and ESC Cardiovascular risk
collaboration (2021) <doi:10.1093/eurheartj/ehab309>. TIMI described in
Antman EM, et al (2000) <doi:10.1001/jama.284.7.835>.

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
