%global packname  GGUM
%global packver   0.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Generalized Graded Unfolding Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-xlsx 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-xlsx 

%description
An implementation of the generalized graded unfolding model (GGUM) in R,
see Roberts, Donoghue, and Laughlin (2000)
<doi:10.1177/01466216000241001>). It allows to simulate data sets based on
the GGUM. It fits the GGUM and the GUM, and it retrieves item and person
parameter estimates. Several plotting functions are available (item and
test information functions; item and test characteristic curves; item
category response curves). Additionally, there are some functions that
facilitate the communication between R and 'GGUM2004'. Finally, a
model-fit checking utility, MODFIT(), is also available.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
