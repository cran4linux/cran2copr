%global __brp_check_rpaths %{nil}
%global packname  kwb.hantush
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Calculation of Groundwater Mounding Beneath an InfiltrationBasin

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-hydroGOF 
Requires:         R-lattice 
Requires:         R-CRAN-hydroGOF 

%description
Calculation groundwater mounding beneath an infiltration basin based on
the Hantush (1967) equation (<doi:10.1029/WR003i001p00227>). The correct
implementation is shown with a verification example based on a USGS report
(page 25,
<https://pubs.usgs.gov/sir/2010/5102/support/sir2010-5102.pdf#page=35>).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
