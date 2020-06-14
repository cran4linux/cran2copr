%global packname  MC2toPath
%global packver   0.0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.16
Release:          2%{?dist}
Summary:          Translates information from netcdf files with MC2 output intointer-PVT transitions.

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RNetCDF 
Requires:         R-CRAN-RNetCDF 

%description
Post processes MC2 output, especially for use by Path or ST-Sim.  MC2
(short for "MC1 version 2") is a dynamic global vegetation model
(en.wikipedia.org/wiki/DGVM).  Path (essa.com/tools/path) and ST-Sim
(www.apexrms.com) are state-and-transition model (STM) engines. MC2 has a
user website at sites.google.com/site/mc1dgvmusers.  Since 2001, MC1 has
been used to simulate changes in natural vegetation due to climate change
at scales from regional to global.  In 2012, MC1 was reimplemented in C++
to make it faster and to reduce storage requirements.  This newer version
is referred to as MC2, an abbreviation of "MC1 version 2".  Beginning in
2011, output from MC1 and MC2 has been used to inform regional
state-and-transition model simulations by the U.S. Forest Service and the
Washington State Department of Natural Resources.  Projects to date have
involved study areas in central Oregon, the Olympic Peninsula, the Blue
Mountains ecoregion, southwestern Oregon, and southeastern Oregon.  In the
first of this series of projects, the netCDF output files from MC2 were
manually post-processed, mostly in Excel, to produce input .csv files for
the STM engines. Beginning with the second project, R scripts were used to
automate the post-processing work.  These R scripts have been collected
into the MC2toPath R-package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/netcdf
%{rlibdir}/%{packname}/INDEX
