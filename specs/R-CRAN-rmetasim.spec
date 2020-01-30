%global packname  rmetasim
%global packver   3.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.13
Release:          1%{?dist}
Summary:          An Individual-Based Population Genetic Simulation Environment

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-adegenet 
Requires:         R-CRAN-pegas 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-adegenet 

%description
An interface between R and the metasim simulation engine. The simulation
environment is documented in: "Strand, A.(2002)
<DOI:10.1046/j.1471-8286.2002.00208.x> Metasim 1.0: an individual-based
environment for simulating population genetics of complex population
dynamics. Mol. Ecol. Notes. Please see the vignettes CreatingLandscapes
and Simulating to get some ideas on how to use the packages. See the
rmetasim vignette to get an overview and to see important changes to the
code in the most recent version.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
