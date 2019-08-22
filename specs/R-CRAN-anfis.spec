%global packname  anfis
%global packver   0.99.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.1
Release:          1%{?dist}
Summary:          Adaptive Neuro Fuzzy Inference System in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-methods 
Requires:         R-parallel 

%description
The package implements ANFIS Type 3 Takagi and Sugeno's fuzzy if-then rule
network with the following features: (1) Independent number of membership
functions(MF) for each input, and also different MF extensible types. (2)
Type 3 Takagi and Sugeno's fuzzy if-then rule (3) Full Rule combinations,
e.g. 2 inputs 2 membership funtions -> 4 fuzzy rules (4) Hibrid learning,
i.e. Descent Gradient for precedents and Least Squares Estimation for
consequents (5) Multiple outputs.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
