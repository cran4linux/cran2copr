%global __brp_check_rpaths %{nil}
%global packname  sindyr
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Sparse Identification of Nonlinear Dynamics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-crqa 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-crqa 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-pracma 

%description
This implements the Brunton et al (2016; PNAS
<doi:10.1073/pnas.1517384113>) sparse identification algorithm for finding
ordinary differential equations for a measured system from raw data
(SINDy). The package includes a set of additional tools for working with
raw data, with an emphasis on cognitive science applications (Dale and
Bhat, in press <doi:10.1016/j.cogsys.2018.06.020>).

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
%{rlibdir}/%{packname}/INDEX
