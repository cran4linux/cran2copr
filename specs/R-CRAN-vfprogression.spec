%global packname  vfprogression
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          3%{?dist}%{?buildtag}
Summary:          Visual Field (VF) Progression Analysis and Plotting Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Realization of published methods to analyze visual field (VF) progression.
Introduction to the plotting methods (designed by author TE) for VF output
visualization. A sample dataset for two eyes, each with 10 follow-ups is
included. The VF analysis methods could be found in -- Musch et al. (1999)
<doi:10.1016/S0161-6420(99)90147-1>, Nouri-Mahdavi et at. (2012)
<doi:10.1167/iovs.11-9021>, Schell et at. (2014)
<doi:10.1016/j.ophtha.2014.02.021>, Aptel et al. (2015)
<doi:10.1111/aos.12788>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
