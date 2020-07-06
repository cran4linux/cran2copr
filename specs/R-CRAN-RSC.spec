%global packname  RSC
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Robust and Sparse Correlation Matrix

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-utils 

%description
Performs robust and sparse correlation matrix estimation. Robustness is
achieved based on a simple robust pairwise correlation estimator, while
sparsity is obtained based on thresholding. The optimal thresholding is
tuned via cross-validation. See Serra, Coretto, Fratello, and Tagliaferri
(2018) <doi:10.1093/bioinformatics/btx642>.

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
