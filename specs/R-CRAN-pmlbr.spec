%global packname  pmlbr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the Penn Machine Learning Benchmarks Data Repository

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-stats 
Requires:         R-utils 
Requires:         R-CRAN-FNN 
Requires:         R-stats 

%description
Check available classification and regression data sets from the PMLB
repository and download them. The PMLB repository
(<https://github.com/EpistasisLab/pmlbr>) contains a curated collection of
data sets for evaluating and comparing machine learning algorithms. These
data sets cover a range of applications, and include binary/multi-class
classification problems and regression problems, as well as combinations
of categorical, ordinal, and continuous features. There are currently over
150 datasets included in the PMLB repository.

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
