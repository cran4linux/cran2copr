%global packname  PooledCohort
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Predict 10-Year Risk for Atherosclerotic Cardiovascular Disease

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-stats 
Requires:         R-CRAN-glue 
Requires:         R-stats 

%description
The 2017 American College of Cardiology and American Heart Association
blood pressure guideline recommends using 10-year predicted
atherosclerotic cardiovascular disease risk to guide the decision to
initiate or intensify antihypertensive medication. The guideline
recommends using the Pooled Cohort risk prediction equations to predict
10-year atherosclerotic cardiovascular disease risk. This package
implements the original Pooled Cohort risk prediction equations and also
incorporates updated versions based on more contemporary data and
statistical methods. References: Goff DC, Lloyd-Jones DM, Bennett G, Coady
S, D’Agostino RB, Gibbons R, Greenland P, Lackland DT, Levy D, O’Donnell
CJ, and Robinson JG (2014) <doi:10.1016/j.jacc.2014.03.006> Yadlowsky S,
Hayward RA, Sussman JB, McClelland RL, Min YI, and Basu S (2018)
<doi:10.7326/m17-3011>.

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
