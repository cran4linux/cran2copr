%global packname  test2norm
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Normative Standards for Cognitive Tests

License:          CPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-mfp 
Requires:         R-CRAN-mfp 

%description
Function test2norm() generates formulas for normative standards applied to
cognitive tests. It takes raw test scores (e.g., number of correct
responses) and converts them to scaled scores and demographically adjusted
scores, using methods described in Heaton et al. (2003)
<doi:10.1016/B978-012703570-3/50010-9> & Heaton et al. (2009,
ISBN:9780199702800). The scaled scores are calculated as quantiles of the
raw test scores, scaled to have the mean of 10 and standard deviation of
3, such that higher values always correspond to better performance on the
test. The demographically adjusted scores are calculated from the
residuals of a model that regresses scaled scores on demographic
predictors (e.g., age). The norming procedure makes use of the mfp()
function from the 'mfp' package to explore nonlinear associations between
cognition and demographic variables.

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
