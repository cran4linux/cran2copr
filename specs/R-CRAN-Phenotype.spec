%global packname  Phenotype
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          A Tool for Phenotypic Data Processing

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-tidyr 

%description
Large-scale phenotypic data processing is essential in research.
Researchers need to eliminate outliers from the data in order to obtain
true and reliable results. Best linear unbiased prediction (BLUP) is a
standard method for estimating random effects of a mixed model. This
method can be used to process phenotypic data under different conditions
and is widely used in animal and plant breeding. The 'Phenotype' can
remove outliers from phenotypic data and performs the best linear unbiased
prediction (BLUP), help researchers quickly complete phenotypic data
analysis. H.P.Piepho. (2008) <doi:10.1007/s10681-007-9449-8>.

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
