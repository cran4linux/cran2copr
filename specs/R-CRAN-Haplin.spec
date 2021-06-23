%global __brp_check_rpaths %{nil}
%global packname  Haplin
%global packver   7.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Case-Parent Triad and/or Case-Control Data with SNP Haplotypes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-tools 
BuildRequires:    R-mgcv 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
Requires:         R-tools 
Requires:         R-mgcv 
Requires:         R-MASS 
Requires:         R-CRAN-ff 
Requires:         R-CRAN-rlang 
Requires:         R-methods 

%description
Performs genetic association analyses of case-parent triad (trio) data
with multiple markers. It can also incorporate complete or incomplete
control triads, for instance independent control children. Estimation is
based on haplotypes, for instance SNP haplotypes, even though phase is not
known from the genetic data. 'Haplin' estimates relative risk (RR +
conf.int.) and p-value associated with each haplotype. It uses maximum
likelihood estimation to make optimal use of data from triads with missing
genotypic data, for instance if some SNPs has not been typed for some
individuals. 'Haplin' also allows estimation of effects of maternal
haplotypes and parent-of-origin effects, particularly appropriate in
perinatal epidemiology. 'Haplin' allows special models, like
X-inactivation, to be fitted on the X-chromosome. A GxE analysis allows
testing interactions between environment and all estimated genetic
effects. The models were originally described in Gjessing, HK and Lie, RT
(2006) <doi:10.1111/j.1529-8817.2005.00218.x>.

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
