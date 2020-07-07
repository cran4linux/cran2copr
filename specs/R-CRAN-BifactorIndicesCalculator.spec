%global packname  BifactorIndicesCalculator
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Bifactor Indices Calculator

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-MplusAutomation 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-MplusAutomation 

%description
The calculator computes bifactor indices such as explained common variance
(ECV), hierarchical Omega (OmegaH), percentage of uncontaminated
correlations (PUC), item explained common variance (I-ECV), and more. This
package is an R version of the 'Excel' based 'Bifactor Indices Calculator'
(Dueber, 2017) <doi:10.13023/edp.tool.01> with added convenience features
for directly utilizing output from several programs that can fit
confirmatory factor analysis or item response models.

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
