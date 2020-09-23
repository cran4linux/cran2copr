%global packname  mrregression
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Analysis for Very Large Data Sets via Merge and Reduce

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-Rcpp >= 1.0.5

%description
Frequentist and Bayesian linear regression for large data sets. Useful
when the data does not fit into memory (for both frequentist and Bayesian
regression), to make running time manageable (mainly for Bayesian
regression), and to reduce the total running time because of reduced or
less severe memory-spillover into the virtual memory. This is an
implementation of Merge & Reduce for linear regression as described in
Geppert, L.N., Ickstadt, K., Munteanu, A., & Sohler, C. (2020). 'Streaming
statistical models via Merge & Reduce'. International Journal of Data
Science and Analytics, 1-17, <doi:10.1007/s41060-020-00226-0>.

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
