%global packname  mstDIF
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          A Collection of DIF Tests for Multistage Tests

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mirt >= 1.31
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-PP 
BuildRequires:    R-CRAN-scDIFtest 
BuildRequires:    R-CRAN-eRm 
Requires:         R-CRAN-mirt >= 1.31
Requires:         R-CRAN-expm 
Requires:         R-Matrix 
Requires:         R-CRAN-PP 
Requires:         R-CRAN-scDIFtest 
Requires:         R-CRAN-eRm 

%description
A collection of statistical tests for the detection of differential item
functioning (DIF) in multistage tests. Methods entail logistic regression,
an adaptation of the simultaneous item bias test (SIBTEST), and various
score-based tests. The presented tests provide itemwise test for DIF along
categorical, ordinal or metric covariates. Methods for uniform and
non-uniform DIF effects are available depending on which method is used.

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
