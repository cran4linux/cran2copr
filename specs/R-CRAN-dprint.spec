%global __brp_check_rpaths %{nil}
%global packname  dprint
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Print Tabular Data to Graphics Device

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Provides a generalized method for printing tabular data within the R
environment in order to make the process of presenting high quality
tabular output seamless for the user.  Output is directed to the R
graphics device so that tables can be exported to any file format
supported by the graphics device. Utilizes a formula interface to specify
the contents of tables often found in manuscripts or business reports.  In
addition, formula interface provides inline formatting of the numeric
cells of a table and renaming column labels.

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
