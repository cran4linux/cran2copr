%global __brp_check_rpaths %{nil}
%global packname  lcra
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Joint Latent Class and Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rjags 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rjags 

%description
For fitting Bayesian joint latent class and regression models using Gibbs
sampling. See the documentation for the model. The technical details of
the model implemented here are described in Elliott, Michael R., Zhao,
Zhangchen, Mukherjee, Bhramar, Kanaya, Alka, Needham, Belinda L., "Methods
to account for uncertainty in latent class assignments when using latent
classes as predictors in regression models, with application to
acculturation strategy measures" (2020) In press at Epidemiology
<doi:10.1097/EDE.0000000000001139>.

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
