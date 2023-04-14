%global __brp_check_rpaths %{nil}
%global packname  MatrixEQTL
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Matrix eQTL: Ultra Fast eQTL Analysis via Large MatrixOperations

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 

%description
Matrix eQTL is designed for fast eQTL analysis on large datasets. Matrix
eQTL can test for association between genotype and gene expression using
linear regression with either additive or ANOVA genotype effects. The
models can include covariates to account for factors as population
stratification, gender, and clinical variables. It also supports models
with heteroscedastic and/or correlated errors, false discovery rate
estimation and separate treatment of local (cis) and distant (trans)
eQTLs. For more details see Shabalin (2012)
<doi:10.1093/bioinformatics/bts163>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
