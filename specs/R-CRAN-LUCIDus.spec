%global packname  LUCIDus
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Latent Unknown Clustering with Integrated Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-parallel 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-lbfgs 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-mclust 
Requires:         R-nnet 
Requires:         R-CRAN-networkD3 
Requires:         R-parallel 
Requires:         R-boot 
Requires:         R-CRAN-lbfgs 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-glmnet 

%description
An implementation for the 'LUCID' model (Peng (2019)
<doi:10.1093/bioinformatics/btz667>) to jointly estimate latent unknown
clusters/subgroups with integrated data. An EM algorithm is used to obtain
the latent cluster assignment and model parameter estimates. Feature
selection is achieved by applying the L1 regularization method.

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
