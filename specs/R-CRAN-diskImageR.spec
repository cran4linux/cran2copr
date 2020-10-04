%global packname  diskImageR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Pipeline to Analyze Resistance and Tolerance from Drug DiskDiffusion Assays

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         imagej
BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-tcltk 
BuildRequires:    R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-subplex 
Requires:         R-tcltk 
Requires:         R-methods 

%description
A pipeline to analyze photographs of disk diffusion plates. This removes
the need to analyze the plates themselves, and thus analysis can be done
separate from the assay. Furthermore, diskImageR removes potential
researcher bias, by quantitative assessment of drug resistance as the zone
diameter at multiple cutoff values of growth inhibition. This method also
extends the disk diffusion assay by measuring drug tolerance (in addition
to drug resistance) as the fraction of the subpopulation that is able to
grow above the resistance point ("FoG"), and drug sensitivity as the rate
of change from no growth to full growth ("slope").

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
%doc %{rlibdir}/%{packname}/diskImageR_vignette.html
%doc %{rlibdir}/%{packname}/IJ_diskImageR.ijm
%doc %{rlibdir}/%{packname}/knownMIC-RAD.csv
%doc %{rlibdir}/%{packname}/walkthrough.R
%{rlibdir}/%{packname}/INDEX
