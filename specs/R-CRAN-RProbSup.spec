%global packname  RProbSup
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          2%{?dist}
Summary:          Calculates Probability of Superiority

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The A() function calculates the A statistic, a nonparametric measure of
effect size for two independent groups that’s also known as the
probability of superiority (Ruscio, 2008), along with its standard error
and a confidence interval constructed using bootstrap methods (Ruscio &
Mullen, 2012). Optional arguments can be specified to calculate variants
of the A statistic developed for other research designs (e.g., related
samples, more than two independent groups or related samples; Ruscio &
Gera, 2013). <DOI: 10.1037/1082-989X.13.1.19>. <DOI:
10.1080/00273171.2012.658329>. <DOI: 10.1080/00273171.2012.738184>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
