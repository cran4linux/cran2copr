%global packname  IRTBEMM
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Family of Bayesian EMM Algorithm for Item Response Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
Applying the family of the Bayesian Expectation-Maximization-Maximization
(BEMM) algorithm to estimate: (1) Three parameter logistic (3PL) model
proposed by Birnbaum (1968, ISBN:9780201043105); (2) four parameter
logistic (4PL) model proposed by Barton & Lord (1981)
<doi:10.1002/j.2333-8504.1981.tb01255.x>; (3) one parameter logistic
guessing (1PLG) and (4) one parameter logistic ability-based guessing
(1PLAG) models proposed by San Martín et al (2006)
<doi:10.1177/0146621605282773>. The BEMM family includes (1) the BEMM
algorithm for 3PL model proposed by Guo & Zheng (2019)
<doi:10.3389/fpsyg.2019.01175>; (2) the BEMM algorithm for 1PLG model and
(3) the Bayesian Expectation-Maximization-Maximization-Maximization (BE3M)
algorithm for 1PLAG model proposed by Guo, Wu, Zheng, & Wang (2018)
<https:www.ncme.org/news/past-meetings/2018-recap>; (4) the BE3M algorithm
for 4PL model proposed by Zhang, Guo, & Zheng (2018)
<https:www.ncme.org/news/past-meetings/2018-recap>; and (5) their maximum
likelihood estimation versions proposed by Zheng, Meng, Guo, & Liu (2018)
<doi:10.3389/fpsyg.2017.02302>. Thus, both Bayesian modal estimates and
maximum likelihood estimates are available.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
