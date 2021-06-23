%global __brp_check_rpaths %{nil}
%global packname  EBPRS
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Derive Polygenic Risk Score Based on Emprical Bayes Theory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BEDMatrix 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-ROCR 
Requires:         R-methods 
Requires:         R-CRAN-BEDMatrix 
Requires:         R-CRAN-data.table 

%description
EB-PRS is a novel method that leverages information for effect sizes
across all the markers to improve the prediction accuracy.  No parameter
tuning is needed in the method, and no external information is needed.
This R-package provides the calculation of polygenic risk scores from the
given training summary statistics and testing data. We can use EB-PRS to
extract main information, estimate Empirical Bayes parameters, derive
polygenic risk scores for each individual in testing data, and evaluate
the PRS according to AUC and predictive r2. See Song et al. (2020)
<doi:10.1371/journal.pcbi.1007565> for a detailed presentation of the
method.

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
