%global packname  eaf
%global packver   1.9-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.1
Release:          1%{?dist}
Summary:          Plots of the Empirical Attainment Function

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-modeltools 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Computation and visualization of the empirical attainment function (EAF)
for the analysis of random sets in multi-criterion optimization. M.
Lopez-Ibanez, L. Paquete, and T. Stuetzle (2010)
<doi:10.1007/978-3-642-02538-9_9>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
