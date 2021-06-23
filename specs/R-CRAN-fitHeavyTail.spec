%global __brp_check_rpaths %{nil}
%global packname  fitHeavyTail
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mean and Covariance Matrix Estimation under Heavy Tails

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ICSNP 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-ICSNP 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 

%description
Robust estimation methods for the mean vector and covariance matrix from
data (possibly containing NAs) under multivariate heavy-tailed
distributions such as angular Gaussian (via Tyler's method), Cauchy, and
Student's t. Additionally, a factor model structure can be specified for
the covariance matrix. The package is based on the papers: Sun, Babu, and
Palomar (2014), Sun, Babu, and Palomar (2015), Liu and Rubin (1995), and
Zhou, Liu, Kumar, and Palomar (2019).

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
