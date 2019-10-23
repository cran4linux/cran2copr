%global packname  smoothAPC
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Smoothing of Two-Dimensional Demographic Data, Optionally Takinginto Account Period and Cohort Effects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-methods 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-lmtest 
Requires:         R-stats 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-colorspace 
Requires:         R-methods 

%description
The implemented method uses for smoothing bivariate thin plate splines,
bivariate lasso-type regularization, and allows for both period and cohort
effects. Thus the mortality rates are modelled as the sum of four
components: a smooth bivariate function of age and time, smooth
one-dimensional cohort effects, smooth one-dimensional period effects and
random errors.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
