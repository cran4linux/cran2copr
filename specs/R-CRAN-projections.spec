%global packname  projections
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          2%{?dist}
Summary:          Project Future Case Incidence

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-incidence >= 1.4.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
Requires:         R-CRAN-incidence >= 1.4.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 

%description
Provides functions and graphics for projecting daily incidence based on
past incidence, and estimates of the serial interval and reproduction
number. Projections are based on a branching process using a
Poisson-distributed number of new cases per day, similar to the model used
for estimating R in 'EpiEstim' or in 'earlyR', and described by Nouvellet
et al. (2017) <doi:10.1016/j.epidem.2017.02.012>. The package provides the
S3 class 'projections' which extends 'matrix', with accessors and
additional helpers for handling, subsetting, merging, or adding these
objects, as well as dedicated printing and plotting methods.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
