%global packname  SIRE
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Finding Feedback Effects in SEM and Testing for TheirSignificance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-systemfit 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-systemfit 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-matrixcalc 
Requires:         R-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-Matrix 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 

%description
Provides two main functionalities. 1 - Given a system of simultaneous
equation, it decomposes the matrix of coefficients weighting the
endogenous variables into three submatrices: one includes the subset of
coefficients that have a causal nature in the model, two include the
subset of coefficients that have a interdependent nature in the model,
either at systematic level or induced by the correlation between error
terms. 2 - Given a decomposed model, it tests for the significance of the
interdependent relationships acting in the system, via Maximum likelihood
and Wald test, which can be built starting from the function output. For
theoretical reference see Faliva (1992) <doi:10.1007/BF02589085> and
Faliva and Zoia (1994) <doi:10.1007/BF02589041>.

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
