%global __brp_check_rpaths %{nil}
%global packname  Cprob
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          The Conditional Probability Function of a Competing Event

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-tpr 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-lgtdl 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-lattice 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-tpr 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-lgtdl 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-lattice 

%description
Permits to estimate the conditional probability function of a competing
event, and to fit, using the temporal process regression or the
pseudo-value approach, a proportional-odds model to the conditional
probability function (or other models by specifying another link
function). See <doi:10.1111/j.1467-9876.2010.00729.x>.

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
