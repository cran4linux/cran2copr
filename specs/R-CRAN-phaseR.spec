%global __brp_check_rpaths %{nil}
%global packname  phaseR
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Phase Plane Analysis of One- And Two-Dimensional Autonomous ODESystems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-deSolve 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Performs a qualitative analysis of one- and two-dimensional autonomous
ordinary differential equation systems, using phase plane methods.
Programs are available to identify and classify equilibrium points, plot
the direction field, and plot trajectories for multiple initial
conditions. In the one-dimensional case, a program is also available to
plot the phase portrait. Whilst in the two-dimensional case, programs are
additionally available to plot nullclines and stable/unstable manifolds of
saddle points. Many example systems are provided for the user. For further
details can be found in Grayling (2014) <doi:10.32614/RJ-2014-023>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
