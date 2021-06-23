%global __brp_check_rpaths %{nil}
%global packname  hydroPSO
%global packver   0.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Particle Swarm Optimisation, with Focus on Environmental Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.2
BuildRequires:    R-CRAN-hydroTSM >= 0.3.6
BuildRequires:    R-CRAN-hydroGOF >= 0.3.5
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-vioplot 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-zoo >= 1.7.2
Requires:         R-CRAN-hydroTSM >= 0.3.6
Requires:         R-CRAN-hydroGOF >= 0.3.5
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-sp 
Requires:         R-lattice 
Requires:         R-grid 
Requires:         R-CRAN-lhs 
Requires:         R-parallel 
Requires:         R-CRAN-vioplot 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-data.table 

%description
State-of-the-art version of the Particle Swarm Optimisation (PSO)
algorithm (SPSO-2011 and SPSO-2007 capable). hydroPSO can be used as a
replacement of the 'optim' R function for (global) optimization of
non-smooth and non-linear functions. However, the main focus of hydroPSO
is the calibration of environmental and other real-world models that need
to be executed from the system console. hydroPSO is model-independent,
allowing the user to easily interface any computer simulation model with
the calibration engine (PSO). hydroPSO communicates with the model through
the model's own input and output files, without requiring access to the
model's source code. Several PSO variants and controlling options are
included to fine-tune the performance of the calibration engine to
different calibration problems. An advanced sensitivity analysis function
together with user-friendly plotting summaries facilitate the
interpretation and assessment of the calibration results. hydroPSO is
parallel-capable, to alleviate the computational burden of complex models
with "long" execution time. Bugs reports/comments/questions are very
welcomed (in English, Spanish or Italian). See Zambrano-Bigiarini and
Rojas (2013) <doi:10.1016/j.envsoft.2013.01.004> for more details.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/hydroPSO2pest.pst
%doc %{rlibdir}/%{packname}/Rscripts
%{rlibdir}/%{packname}/INDEX
