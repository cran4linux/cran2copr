%global __brp_check_rpaths %{nil}
%global packname  shelltrace
%global packver   3.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bivalve Growth and Trace Element Accumulation Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-bmp 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-bmp 
Requires:         R-CRAN-tiff 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Contains all the formulae of the growth and trace element uptake model
described in the equally-named Geoscientific Model Development paper (de
Winter, 2017, <doi:10.5194/gmd-2017-137>). The model takes as input a file
with X- and Y-coordinates of digitized growth increments recognized on a
longitudinal cross section through the bivalve shell, as well as a BMP
file of an elemental map of the cross section surface with chemically
distinct phases separated by phase analysis. It proceeds by a step-by-step
process described in the paper, by which digitized growth increments are
used to calculate changes in shell height, shell thickness, shell volume,
shell mass and shell growth rate through the bivalve's life time. Then,
results of this growth modelling are combined with the trace element
mapping results to trace the incorporation of trace elements into the
bivalve shell. Results of various modelling parameters can be exported in
the form of XLSX files.

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
