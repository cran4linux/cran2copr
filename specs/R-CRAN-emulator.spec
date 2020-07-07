%global packname  emulator
%global packver   1.2-20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.20
Release:          3%{?dist}
Summary:          Bayesian Emulation of Computer Programs

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
Allows one to estimate the output of a computer program, as a function of
the input parameters, without actually running it. The computer program is
assumed to be a Gaussian process, whose parameters are estimated using
Bayesian techniques that give a PDF of expected program output.  This PDF
is conditional on a training set of runs, each consisting of a point in
parameter space and the model output at that point.  The emphasis is on
complex codes that take weeks or months to run, and that have a large
number of undetermined input parameters; many climate prediction models
fall into this class.  The emulator essentially determines Bayesian
posterior estimates of the PDF of the output of a model, conditioned on
results from previous runs and a user-specified prior linear model.  A
vignette is provided and the help pages include examples.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
