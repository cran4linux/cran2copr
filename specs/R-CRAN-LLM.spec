%global packname  LLM
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Logit Leaf Model Classifier for Binary Classification

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RWeka 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-reghelper 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-partykit 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RWeka 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-reghelper 
Requires:         R-CRAN-scales 

%description
Fits the Logit Leaf Model, makes predictions and visualizes the output.
(De Caigny et al., (2018) <DOI:10.1016/j.ejor.2018.02.009>).

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

%files
%{rlibdir}/%{packname}
