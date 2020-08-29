%global packname  survxai
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of the Local and Global Survival ModelExplanations

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-breakDown 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-survminer 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-breakDown 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-scales 
Requires:         R-survival 
Requires:         R-CRAN-survminer 

%description
Survival models may have very different structures. This package contains
functions for creating a unified representation of a 'survival' models,
which can be further processed by various survival explainers. Tools
implemented in 'survxai' help to understand how input variables are used
in the model and what impact do they have on the final model prediction.
Currently, four explanation methods are implemented. We can divide them
into two groups: local and global. Explanations of the methods can be
found in Grudziaz et al.(2018) <doi:10.21105/joss.00961>.

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
